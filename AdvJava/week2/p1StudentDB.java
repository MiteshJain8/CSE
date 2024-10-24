package AdvJava.week2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class p1StudentDB {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/dbName"; // Update this
    private static final String USER = "root"; // Update this
    private static final String PASS = ""; // Update this

    public static void main(String[] args) {
        Connection connection = null;
        Statement statement = null;

        try {
            // Establish the connection
            connection = DriverManager.getConnection(DB_URL, USER, PASS);
            statement = connection.createStatement();

            // Create the students table if it does not exist
            String createTableSQL = "CREATE TABLE IF NOT EXISTS students (" +
                    "USN VARCHAR(20) PRIMARY KEY, " +
                    "Name VARCHAR(100), " +
                    "Semester INT, " +
                    "CGPA FLOAT)";
            statement.executeUpdate(createTableSQL);
            System.out.println("Table 'students' created or already exists.");

            // Insert sample data
            String insertDataSQL = "INSERT INTO students (USN, Name, Semester, CGPA) VALUES " +
                    "('1MS22CS301', 'Anika Sharma', 5, 8.5), " +
                    "('1MS22CS302', 'Rahul Patel', 5, 7.5), " +
                    "('1MS23CS303', 'Priya Gupta', 3, 9.0), " +
                    "('1MS22CS304', 'Vivek Kumar', 5, 8.0), " +
                    "('1MS22CS305', 'Neha Singh', 3, 8.3), " +
                    "('1MS22CS306', 'Amit Mishra', 5, 9.2), " +
                    "('1MS21CS307', 'Meera Nair', 7, 7.9), " +
                    "('1MS22CS308', 'Rohan Raj', 5, 8.1)";
            statement.executeUpdate(insertDataSQL);
            System.out.println("Sample data inserted into 'students' table.");

            // i. Display details of all the students
            String queryAllStudents = "SELECT * FROM students";
            ResultSet rsAll = statement.executeQuery(queryAllStudents);
            System.out.println("\nAll Students:");
            while (rsAll.next()) {
                System.out.println("USN: " + rsAll.getString("USN") +
                        ", Name: " + rsAll.getString("Name") +
                        ", Semester: " + rsAll.getInt("Semester") +
                        ", CGPA: " + rsAll.getFloat("CGPA"));
            }

            // ii. Display details of all the students who are in the 5th Semester
            String queryFifthSemester = "SELECT * FROM students WHERE Semester = 5";
            ResultSet rsFifth = statement.executeQuery(queryFifthSemester);
            System.out.println("\nStudents in 5th Semester:");
            while (rsFifth.next()) {
                System.out.println("USN: " + rsFifth.getString("USN") +
                        ", Name: " + rsFifth.getString("Name") +
                        ", CGPA: " + rsFifth.getFloat("CGPA"));
            }

            // iii. Display details of all students who have CGPA above 8.0 and are in 5th Semester
            String queryHighCGPA = "SELECT * FROM students WHERE CGPA > 8.0 AND Semester = 5";
            ResultSet rsHighCGPA = statement.executeQuery(queryHighCGPA);
            System.out.println("\nStudents with CGPA > 8.0 in 5th Semester:");
            while (rsHighCGPA.next()) {
                System.out.println("USN: " + rsHighCGPA.getString("USN") +
                        ", Name: " + rsHighCGPA.getString("Name") +
                        ", CGPA: " + rsHighCGPA.getFloat("CGPA"));
            }

            // iv. Display the total number of students who have CGPA above 8.0
            String queryTotalHighCGPA = "SELECT COUNT(*) AS total FROM students WHERE CGPA > 8.0";
            ResultSet rsTotal = statement.executeQuery(queryTotalHighCGPA);
            if (rsTotal.next()) {
                System.out.println("\nTotal number of students with CGPA > 8.0: " + rsTotal.getInt("total"));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Close resources
            try {
                if (statement != null)
                    statement.close();
                if (connection != null)
                    connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}