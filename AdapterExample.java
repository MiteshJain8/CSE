import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JFrame;
import javax.swing.JPanel;

// Custom JPanel class with mouse event handling
class CustomPanel extends JPanel {
    public CustomPanel() {
        // Register a mouse listener for mouse events
        addMouseListener(new CustomMouseListener());
    }
    
    // Custom mouse listener class extending MouseAdapter
    private class CustomMouseListener extends MouseAdapter {
        @Override
        public void mouseClicked(MouseEvent e) {
            // Handle mouse clicked event
            System.out.println("Mouse clicked at: (" + e.getX() + ", " + e.getY() + ")");
        }
    }
}

public class AdapterExample {
    public static void main(String[] args) {
        // Create a JFrame
        JFrame frame = new JFrame("Adapter Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Add a custom panel to the frame
        frame.add(new CustomPanel());
        
        // Set the size of the frame and make it visible
        frame.setSize(300, 200);
        frame.setVisible(true);
    }
}
