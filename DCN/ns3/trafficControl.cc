#include "ns3/applications-module.h"
#include "ns3/core-module.h" 
#include "ns3/flow-monitor-module.h" 
#include "ns3/internet-module.h" 
#include "ns3/network-module.h" 
#include "ns3/point-to-point-module.h" 
#include "ns3/traffic-control-module.h" 
// This simple example shows how to use TrafficControlHelper to install a QueueDisc on a device. 
// The default QueueDisc is a pfifo_fast with a capacity of 1000 packets (as in Linux). 
// However, in this example, we install a RedQueueDisc with a capacity of 10000 packets. 
// Network topology 
// 10.1.1.0 
// n0 -------------- n1 
// point-to-point 
using namespace ns3; 
NS_LOG_COMPONENT_DEFINE("TrafficControlExample"); 
/** 
* Number of packets in TX queue trace. 
* 
* \param oldValue Old value. 
* \param newValue New value. 
*/ 
void TcPacketsInQueueTrace(uint32_t oldValue, uint32_t newValue) 
{ 
std::cout << "TcPacketsInQueue " << oldValue << " to " << newValue << std::endl; 
} 
/** 
* Packets in the device queue trace. 
* 
* \param oldValue Old value. 
* \param newValue New value. 
*/ 
void DevicePacketsInQueueTrace(uint32_t oldValue, uint32_t newValue) 
{ 
std::cout << "DevicePacketsInQueue " << oldValue << " to " << newValue << std::endl; 
} 
/** 
* TC Sojourn time trace. 
* 
* \param sojournTime The sojourn time. 
*/ 
void SojournTimeTrace(Time sojournTime) 
{ 
std::cout << "Sojourn time " << sojournTime.ToDouble(Time::MS) << "ms" << std::endl; 
} 
int main(int argc, char *argv[]) 
{ 
double simulationTime = 10; // seconds 
std::string transportProt = "Tcp"; // Default transport protocol 
std::string socketType; 
// Parse command line arguments 
CommandLine cmd(__FILE__); 
cmd.AddValue("transportProt", "Transport protocol to use: Tcp, Udp", transportProt); 
cmd.Parse(argc, argv); 
// Set socket type based on transport protocol 
if (transportProt == "Tcp") 
{ 
socketType = "ns3::TcpSocketFactory"; 
} 
else 
{ 
socketType = "ns3::UdpSocketFactory"; 
} 
// Create nodes 
NodeContainer nodes; 
nodes.Create(2); 
// Configure point-to-point link 
PointToPointHelper pointToPoint; 
pointToPoint.SetDeviceAttribute("DataRate", StringValue("10Mbps")); 
pointToPoint.SetChannelAttribute("Delay", StringValue("2ms")); 
pointToPoint.SetQueue("ns3::DropTailQueue", "MaxSize", StringValue("1p")); 
// Install devices on nodes 
NetDeviceContainer devices; 
devices = pointToPoint.Install(nodes); 
// Install Internet stack on nodes 
InternetStackHelper stack; 
stack.Install(nodes); 
// Set up traffic control helper 
TrafficControlHelper tch; 
tch.SetRootQueueDisc("ns3::RedQueueDisc"); 
QueueDiscContainer qdiscs = tch.Install(devices); 
// Trace number of packets in the Traffic Control queue 
Ptr<QueueDisc> q = qdiscs.Get(1); 
q->TraceConnectWithoutContext("PacketsInQueue", 
MakeCallback(&TcPacketsInQueueTrace)); 
// Trace Sojourn time 
Config::ConnectWithoutContext("/NodeList/1/$ns3::TrafficControlLayer/RootQueueDiscList/0/So 
journTime", 
MakeCallback(&SojournTimeTrace)); 
// Trace number of packets in the NetDevice queue 
Ptr<NetDevice> nd = devices.Get(1); 
Ptr<PointToPointNetDevice> ptpnd = DynamicCast<PointToPointNetDevice>(nd); 
Ptr<Queue<Packet>> queue = ptpnd->GetQueue(); 
queue->TraceConnectWithoutContext("PacketsInQueue", 
MakeCallback(&DevicePacketsInQueueTrace)); 
// Assign IP addresses to the devices 
Ipv4AddressHelper address; 
address.SetBase("10.1.1.0", "255.255.255.0"); 
Ipv4InterfaceContainer interfaces = address.Assign(devices); 
// Set up and install packet sink application on node 0 
uint16_t port = 7; 
Address localAddress(InetSocketAddress(Ipv4Address::GetAny(), port)); 
PacketSinkHelper packetSinkHelper(socketType, localAddress); 
ApplicationContainer sinkApp = packetSinkHelper.Install(nodes.Get(0)); 
sinkApp.Start(Seconds(0.0)); 
sinkApp.Stop(Seconds(simulationTime + 0.1)); 
// Configure and install OnOff application on node 1 
uint32_t payloadSize = 1448; 
Config::SetDefault("ns3::TcpSocket::SegmentSize", UintegerValue(payloadSize)); 
OnOffHelper onoff(socketType, Ipv4Address::GetAny()); 
onoff.SetAttribute("OnTime", StringValue("ns3::ConstantRandomVariable[Constant=1]")); 
onoff.SetAttribute("OffTime", StringValue("ns3::ConstantRandomVariable[Constant=0]")); 
onoff.SetAttribute("PacketSize", UintegerValue(payloadSize)); 
onoff.SetAttribute("DataRate", StringValue("50Mbps")); // bit/s 
ApplicationContainer apps; 
InetSocketAddress rmt(interfaces.GetAddress(0), port); 
rmt.SetTos(0xb8); 
AddressValue remoteAddress(rmt); 
onoff.SetAttribute("Remote", remoteAddress); 
apps.Add(onoff.Install(nodes.Get(1))); 
apps.Start(Seconds(1.0)); 
apps.Stop(Seconds(simulationTime + 0.1)); 
// Install FlowMonitor on all nodes 
FlowMonitorHelper flowmon; 
Ptr<FlowMonitor> monitor = flowmon.InstallAll(); 
// Run the simulator 
Simulator::Stop(Seconds(simulationTime + 5)); 
Simulator::Run(); 
// Gather flow monitor statistics 
Ptr<Ipv4FlowClassifier> classifier = 
DynamicCast<Ipv4FlowClassifier>(flowmon.GetClassifier()); 
std::map<FlowId, FlowMonitor::FlowStats> stats = monitor->GetFlowStats(); 
std::cout << std::endl << "*** Flow monitor statistics ***" << std::endl; 
std::cout << " Tx Packets/Bytes: " << stats[1].txPackets << " / " << stats[1].txBytes << 
std::endl; 
std::cout << " Offered Load: " << stats[1].txBytes * 8.0 / 
(stats[1].timeLastTxPacket.GetSeconds() - stats[1].timeFirstTxPacket.GetSeconds()) / 1000000 
<< " Mbps" << std::endl; 
std::cout << " Rx Packets/Bytes: " << stats[1].rxPackets << " / " << stats[1].rxBytes << 
std::endl; 
// Calculate and print packets dropped by Queue Disc and NetDevice 
uint32_t packetsDroppedByQueueDisc = 0; 
uint64_t bytesDroppedByQueueDisc = 0; 
if (stats[1].packetsDropped.size() > Ipv4FlowProbe::DROP_QUEUE_DISC) 
{ 
packetsDroppedByQueueDisc = 
stats[1].packetsDropped[Ipv4FlowProbe::DROP_QUEUE_DISC]; 
bytesDroppedByQueueDisc = 
stats[1].bytesDropped[Ipv4FlowProbe::DROP_QUEUE_DISC]; 
} 
std::cout << " Packets/Bytes Dropped by Queue Disc: " << packetsDroppedByQueueDisc << 
" / " << bytesDroppedByQueueDisc << std::endl; 
uint32_t packetsDroppedByNetDevice = 0; 
uint64_t bytesDroppedByNetDevice = 0; 
if (stats[1].packetsDropped.size() > Ipv4FlowProbe::DROP_QUEUE) 
{ 
packetsDroppedByNetDevice = stats[1].packetsDropped[Ipv4FlowProbe::DROP_QUEUE]; 
bytesDroppedByNetDevice = stats[1].bytesDropped[Ipv4FlowProbe::DROP_QUEUE]; 
} 
std::cout << " Packets/Bytes Dropped by NetDevice: " << packetsDroppedByNetDevice << " / 
" << bytesDroppedByNetDevice << std::endl; 
// Print throughput, mean delay, and mean jitter 
std::cout << " Throughput: " << stats[1].rxBytes * 8.0 / 
(stats[1].timeLastRxPacket.GetSeconds() - stats[1].timeFirstRxPacket.GetSeconds()) / 1000000 
<< " Mbps" << std::endl; 
std::cout << " Mean delay: " << stats[1].delaySum.GetSeconds() / stats[1].rxPackets << 
std::endl; 
std::cout << " Mean jitter: " << stats[1].jitterSum.GetSeconds() / (stats[1].rxPackets - 1) << 
std::endl; 
// Print DSCP values 
auto dscpVec = classifier->GetDscpCounts(1); 
for (auto p : dscpVec) 
{ 
std::cout << " DSCP value: 0x" << std::hex << static_cast<uint32_t>(p.first) << std::dec << 
" count: " << p.second << std::endl; 
} 
// Destroy the simulator 
Simulator::Destroy(); 
// Application statistics 
std::cout << std::endl << "*** Application statistics ***" << std::endl; 
double thr = 0; 
uint64_t totalPacketsThr = DynamicCast<PacketSink>(sinkApp.Get(0))->GetTotalRx(); 
thr = totalPacketsThr * 8 / (simulationTime * 1000000.0); // Mbit/s 
std::cout << " Rx Bytes: " << totalPacketsThr << std::endl; 
std::cout << " Average Goodput: " << thr << " Mbit/s" << std::endl; 
// Traffic Control Layer statistics 
std::cout << std::endl << "*** TC Layer statistics ***" << std::endl; 
std::cout << q->GetStats() << std::endl; 
return 0; 
} 