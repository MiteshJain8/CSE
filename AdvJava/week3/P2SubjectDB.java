package AdvJava.week3;

import java.sql.*;

public class P2SubjectDB {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/dbName", USER = "root", PASS = ""; // Update this

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        PreparedStatement pStmt = null;

        try {
            // Establish the connection
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_UPDATABLE);

            // Create the Subject table if it does not exist
            String createTableSQL = "CREATE TABLE IF NOT EXISTS Subject (" +
                    "Code VARCHAR(10) PRIMARY KEY, " +
                    "Name VARCHAR(100), " +
                    "Department VARCHAR(100), " +
                    "Credits INT)";
            stmt.executeUpdate(createTableSQL);
            System.out.println("Table 'Subject' created or already exists.");
            
            // Insert sample data
            String insertDataSQL = "INSERT INTO Subject (Code, Name, Department, Credits) VALUES " +
                    "('CS50', 'System Programming', 'CSE', 3), " +
                    "('CSL57', 'Database Sys Lab', 'CSE', 1), " +
                    "('CSL56', 'Java  Programming  Lab', 'CSE', 1), " +
                    "('HS59', 'Environmental Studies', 'Civil', 0)";
            stmt.executeUpdate(insertDataSQL);
            System.out.println("Sample data inserted into 'Subject' table.");

            // i. Update the Name of the subject from “Java Programming Lab” to “Advanced Java Programming Lab” with Code as CSL56
            String selectSQL = "SELECT * FROM Subject WHERE Code = 'CSL56'";
            ResultSet rs = stmt.executeQuery(selectSQL);
            if (rs.next()) {
                rs.updateString("Name", "Adv Java Prog Lab");
                rs.updateRow();
                System.out.println("\nSubject name updated successfully.");
            }

            // ii. Delete the subject “System Programming” from the table. Use PreparedStatement Object
            String deleteSQL = "DELETE FROM Subject WHERE Name = ?";
            pStmt = conn.prepareStatement(deleteSQL);
            pStmt.setString(1, "System Programming");
            int rowsAffected = pStmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("\nSubject 'System Programming' deleted successfully.");
            } else {
                System.out.println("\nSubject 'System Programming' not found.");
            }

            // iii. Display details of all the Subjects
            String queryAllSubjects = "SELECT * FROM Subject";
            rs = stmt.executeQuery(queryAllSubjects);
            System.out.println("\nCode\tName\t\t\tDepartment\tCredits");
            while (rs.next()) {
                System.out.println(rs.getString("Code") + "\t" +
                        rs.getString("Name") + "\t" +
                        rs.getString("Department") + "\t\t" +
                        rs.getInt("Credits"));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Close resources
            try {
                if (stmt != null)
                    stmt.close();
                if (pStmt != null)
                    pStmt.close();
                if (conn != null)
                    conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

}