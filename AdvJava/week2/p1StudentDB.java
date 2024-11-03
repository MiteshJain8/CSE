package AdvJava.week2;

import java.sql.*;

public class P1StudentDB {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/dbName", USER = "root", PASS = ""; // Update this

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;

        try {
            // Establish the connection
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            stmt = conn.createStatement();

            // Create the students table if it does not exist
            String createTableSQL = "CREATE TABLE IF NOT EXISTS students (" +
                    "USN VARCHAR(20) PRIMARY KEY, " +
                    "Name VARCHAR(100), " +
                    "Semester INT, " +
                    "CGPA FLOAT)";
            stmt.executeUpdate(createTableSQL);
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
            stmt.executeUpdate(insertDataSQL);
            System.out.println("Sample data inserted into 'students' table.");

            // i. Display details of all the students
            String queryAllStudents = "SELECT * FROM students";
            ResultSet rsAll = stmt.executeQuery(queryAllStudents);
            System.out.println("\nAll Students:");
            System.out.println("USN\t\tName\t\tSemester\tCGPA");
            while (rsAll.next()) {
                System.out.println(rsAll.getString("USN") + "\t" +
                        rsAll.getString("Name") + "\t" +
                        rsAll.getInt("Semester") + "\t\t" +
                        rsAll.getFloat("CGPA"));
            }

            // ii. Display details of all the students who are in the 5th Semester
            String queryFifthSemester = "SELECT * FROM students WHERE Semester = 5";
            ResultSet rsFifth = stmt.executeQuery(queryFifthSemester);
            System.out.println("\nStudents in 5th Semester:");
            System.out.println("USN\t\tName\t\tCGPA");
            while (rsFifth.next()) {
                System.out.println(rsFifth.getString("USN") + "\t" +
                        rsFifth.getString("Name") + "\t" +
                        rsFifth.getFloat("CGPA"));
            }

            // iii. Display details of all students who have CGPA above 8.0 and are in 5th Semester
            String queryHighCGPA = "SELECT * FROM students WHERE CGPA > 8.0 AND Semester = 5";
            ResultSet rsHighCGPA = stmt.executeQuery(queryHighCGPA);
            System.out.println("\nStudents with CGPA > 8.0 in 5th Semester:");
            System.out.println("USN\t\tName\t\tCGPA");
            while (rsHighCGPA.next()) {
                System.out.println(rsHighCGPA.getString("USN") + "\t" +
                        rsHighCGPA.getString("Name") + "\t" +
                        rsHighCGPA.getFloat("CGPA"));
            }

            // iv. Display the total number of students who have CGPA above 8.0
            String queryTotalHighCGPA = "SELECT COUNT(*) AS total FROM students WHERE CGPA > 8.0";
            ResultSet rsTotal = stmt.executeQuery(queryTotalHighCGPA);
            if (rsTotal.next()) {
                System.out.println("\nTotal number of students with CGPA > 8.0: " + rsTotal.getInt("total"));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Close resources
            try {
                if (stmt != null)
                    stmt.close();
                if (conn != null)
                    conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}