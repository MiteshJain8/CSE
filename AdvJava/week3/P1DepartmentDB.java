package AdvJava.week3;

import java.sql.*;
import java.util.Scanner;

public class P1DepartmentDB {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/dbName", USER = "root", PASS = ""; // Update this

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        Scanner sc = new Scanner(System.in);

        try {
            // Establish the connection
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            stmt = conn.createStatement();

            // Create the Department table if it does not exist
            String createTableSQL = "CREATE TABLE IF NOT EXISTS Department (" +
                    "Dept_ID INT PRIMARY KEY, " +
                    "Name VARCHAR(100), " +
                    "Year_Established INT, " +
                    "Head_Name VARCHAR(100), " +
                    "No_of_Employees INT)";
            stmt.executeUpdate(createTableSQL);
            System.out.println("Table 'Department' created or already exists.");

            // Insert sample data
            String insertDataSQL = "INSERT INTO Department (Dept_ID, Name, Year_Established, Head_Name, No_of_Employees) VALUES " +
                    "(1, 'CSE', 2000, 'Anika', 30), " +
                    "(2, 'ISE', 2000, 'Rahul', 33), " +
                    "(3, 'Mech', 1995, 'Priya', 29), " +
                    "(4, 'Civil', 1995, 'Vivek', 35)";
            stmt.executeUpdate(insertDataSQL);
            System.out.println("Sample data inserted into 'Department' table.");

            // i. Display details of all the Departments using Statement Object
            String queryAllDepartments = "SELECT * FROM Department";
            try (ResultSet rsAll = stmt.executeQuery(queryAllDepartments)) {
                System.out.println("\nAll Departments:");
                printResultSet(rsAll);
            }

            // ii. Display details of all the Departments which are established in the year 2000 using PreparedStatement object
            System.out.print("\nEnter the year to filter departments: ");
            int year = sc.nextInt();
            String queryByYear = "SELECT * FROM Department WHERE Year_Established = ?";
            try (PreparedStatement pStmt = conn.prepareStatement(queryByYear)) {
                pStmt.setInt(1, year);
                try (ResultSet rsByYear = pStmt.executeQuery()) {
                    System.out.println("\nDepartments established in the year " + year + ":");
                    printResultSet(rsByYear);
                }
            }

            // iii. Display details of all Departments by reading Dept_ID and Department Name from the user using PreparedStatement object
            System.out.print("\nEnter Dept_ID to filter departments: ");
            int deptId = sc.nextInt();
            sc.nextLine(); // Consume newline
            System.out.print("Enter Department Name to filter departments: ");
            String deptName = sc.nextLine();
            String queryByIdAndName = "SELECT * FROM Department WHERE Dept_ID = ? AND Name = ?";
            try (PreparedStatement pStmt = conn.prepareStatement(queryByIdAndName)) {
                pStmt.setInt(1, deptId);
                pStmt.setString(2, deptName);
                try (ResultSet rsByIdAndName = pStmt.executeQuery()) {
                    System.out.println("\nDepartments with Dept_ID " + deptId + " and Name " + deptName + ":");
                    printResultSet(rsByIdAndName);
                }
            }

            // iv. Insert a new row using PreparedStatement object. Display the details
            System.out.print("\nEnter new Dept_ID: ");
            int newDeptId = sc.nextInt();
            sc.nextLine(); // Consume newline
            System.out.print("Enter new Department Name: ");
            String newDeptName = sc.nextLine();
            System.out.print("Enter Year Established: ");
            int newYearEstablished = sc.nextInt();
            sc.nextLine(); // Consume newline
            System.out.print("Enter Head Name: ");
            String newHeadName = sc.nextLine();
            System.out.print("Enter Number of Employees: ");
            int newNoOfEmployees = sc.nextInt();

            String insertSQL = "INSERT INTO Department (Dept_ID, Name, Year_Established, Head_Name, No_of_Employees) VALUES (?, ?, ?, ?, ?)";
            try (PreparedStatement pStmt = conn.prepareStatement(insertSQL)) {
                pStmt.setInt(1, newDeptId);
                pStmt.setString(2, newDeptName);
                pStmt.setInt(3, newYearEstablished);
                pStmt.setString(4, newHeadName);
                pStmt.setInt(5, newNoOfEmployees);
                pStmt.executeUpdate();
                System.out.println("New department inserted successfully.");
            }

            // Display the inserted row
            String queryNewDept = "SELECT * FROM Department WHERE Dept_ID = ?";
            try (PreparedStatement pStmt = conn.prepareStatement(queryNewDept)) {
                pStmt.setInt(1, newDeptId);
                try (ResultSet rsNewDept = pStmt.executeQuery()) {
                    System.out.println("\nInserted Department:");
                    printResultSet(rsNewDept);
                }
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
            sc.close();
        }
    }
    
    private static void printResultSet(ResultSet rs) throws SQLException {
        System.out.println("ID\tName\tYear_Established\tHead_Name\tNo_of_Employees");
        while (rs.next()) {
            System.out.println(rs.getInt("Dept_ID") + "\t" +
                    rs.getString("Name") + "\t\t" +
                    rs.getInt("Year_Established") + "\t\t" +
                    rs.getString("Head_Name") + "\t\t" +
                    rs.getInt("No_of_Employees"));
        }
    }
}
