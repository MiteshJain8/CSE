import java.util.Scanner;

class Invoice {
	private int id;
	private String name;
	private int item_type;
	private int quantity;
	private double price;
	
	void getDetails() {
		System.out.println("id = "+id+"\nname = "+name+
				"\ntype = "+item_type+"\nquantity = "+quantity+
				"\nprice = "+price);
	}
	
	void setDetails() {
		Scanner in = new Scanner(System.in);
		System.out.println("Enter id, name, item type, quantity, price");
		id = in.nextInt();
		name = in.next();
		item_type = in.nextInt();
		quantity = in.nextInt();
		price = in.nextDouble();
		in.close();
	}
	
	private double tax(int item_type, double price) {
		double tax;
		if (item_type == 1) {
			tax = price*0.05;
		}
		else if (item_type == 2) {
			tax = price * 0.12;
		}
		else if (item_type==3) {
			tax = price*0.18;
		}
		else {
			tax = price*0.28;
		}
		return tax;
	}
	
	void printInvoice() {
		double tax = tax(item_type,price);
		System.out.println("Total price = "+(price+tax)*quantity);
	}
}

public class p1 {
	public static void main(String[] args) {
		Invoice i = new Invoice();
		i.setDetails();
		i.getDetails();
		i.printInvoice();
	}
}
