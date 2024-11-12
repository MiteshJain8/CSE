package AdvJava.week4;

import java.sql.*;

public class P2BankAccountDB {

    // Database URL, username, and password
    private static final String DB_URL = "jdbc:mysql://localhost:3307/week4", USER = "root", PASS = ""; // Update this

    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement pStmt = null;
        Statement stmt = null;

        try {
            // Establish the connection
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            stmt = conn.createStatement();

            // Create the Bank_Account table if it does not exist
            String createTableSQL = "CREATE TABLE IF NOT EXISTS Bank_Account (" +
                    "Account_No INT PRIMARY KEY, " +
                    "Account_Name VARCHAR(100), " +
                    "Type_of_Account VARCHAR(50), " +
                    "Balance INT)";
            stmt.executeUpdate(createTableSQL);
            System.out.println("Table 'Bank_Account' created or already exists.");

            // i. Insert rows using PreparedStatement
            String insertSQL = "INSERT INTO Bank_Account (Account_No, Account_Name, Type_of_Account, Balance) VALUES (?, ?, ?, ?)";
            pStmt = conn.prepareStatement(insertSQL);
            pStmt.setInt(1, 1);
            pStmt.setString(2, "Raj");
            pStmt.setString(3, "Savings");
            pStmt.setInt(4, 1500);
            pStmt.executeUpdate();

            pStmt.setInt(1, 2);
            pStmt.setString(2, "Riya");
            pStmt.setString(3, "Current");
            pStmt.setInt(4, 2500);
            pStmt.executeUpdate();

            System.out.println("Sample data inserted into 'Bank_Account' table.");

            // ii. Display details of all the Accounts
            String queryAllAccounts = "SELECT * FROM Bank_Account";
            ResultSet rs = stmt.executeQuery(queryAllAccounts);
            printAccountResultSet(rs);

            // iii. Demonstrate the Working of Rollback and Commit
            conn.setAutoCommit(false);
            try {
                pStmt.setInt(1, 6);
                pStmt.setString(2, "Anu");
                pStmt.setString(3, "Savings");
                pStmt.setInt(4, 500);
                pStmt.executeUpdate();

                pStmt.setInt(1, 7);
                pStmt.setString(2, "Sam");
                pStmt.setString(3, "Current");
                pStmt.setInt(4, 700);
                pStmt.executeUpdate();

                System.out.println("\nRows inserted, committing transaction.");
                conn.commit();
            } catch (SQLException e) {
                System.out.println("\nException occurred, rolling back transaction.");
                conn.rollback();
                e.printStackTrace();
            }

            // iv. Demonstrate the Working of SavePoints
            Savepoint savepoint1 = conn.setSavepoint("Savepoint1");
            try {
                pStmt.setInt(1, 8);
                pStmt.setString(2, "Tanu");
                pStmt.setString(3, "Savings");
                pStmt.setInt(4, 900);
                pStmt.executeUpdate();

                pStmt.setInt(1, 9);
                pStmt.setString(2, "Tarun");
                pStmt.setString(3, "Current");
                pStmt.setInt(4, 1100);
                pStmt.executeUpdate();

                System.out.println("\nRows inserted, rolling back to Savepoint1.");
                conn.rollback(savepoint1);

                System.out.println("\nRows inserted, committing transaction.");
                conn.commit();
            } catch (SQLException e) {
                System.out.println("\nException occurred, rolling back transaction.");
                conn.rollback();
                e.printStackTrace();
            }

            // Display all the details after rollback and commit
            rs = stmt.executeQuery(queryAllAccounts);
            printAccountResultSet(rs);

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

    private static void printAccountResultSet(ResultSet rs) throws SQLException {
        System.out.println("\nAccount_No\tAccount_Name\tType_of_Account\tBalance");
        while (rs.next()) {
            System.out.println(rs.getInt("Account_No") + "\t" +
                    rs.getString("Account_Name") + "\t" +
                    rs.getString("Type_of_Account") + "\t" +
                    rs.getInt("Balance"));
        }
    }
}