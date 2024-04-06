import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GenderApp extends JFrame implements ActionListener {
    private JButton boyButton;
    private JButton girlButton;

    public GenderApp() {
        // Set the title and layout manager for the JFrame
        setTitle("Gender App");
        setLayout(new FlowLayout());

        // Create Boy button and add action listener
        boyButton = new JButton("Boy");
        boyButton.addActionListener(this); // Register the action listener
        add(boyButton); // Add the button to the JFrame

        // Create Girl button and add action listener
        girlButton = new JButton("Girl");
        girlButton.addActionListener(this); // Register the action listener
        add(girlButton); // Add the button to the JFrame

        // Set JFrame properties
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 200);
        setLocationRelativeTo(null); // Center the JFrame on the screen
        setVisible(true); // Make the JFrame visible
    }

    // ActionListener implementation to handle button clicks
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == boyButton) {
            JOptionPane.showMessageDialog(this, "I am a BOY");
        } else if (e.getSource() == girlButton) {
            JOptionPane.showMessageDialog(this, "I am a GIRL");
        }
    }

    public static void main(String[] args) {
        // Create an instance of the GenderApp class
        SwingUtilities.invokeLater(() -> new GenderApp());
    }
}
