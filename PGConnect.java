import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;
import java.util.logging.*;

public class PGConnect {

    private final static Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private Connection connect() {

        final String url = "jdbc:postgresql://edatabases.appdomain.cloud:30352/ibmclouddb";

        Properties props = new Properties();
        props.setProperty("user","admin");
        props.setProperty("password","mypassword123");

        Connection conn = null;
        while (conn == null) {
            try {
                conn = DriverManager.getConnection(url, props);
                System.out.println("Connected to PG");
            } catch (SQLException e) {
                System.out.printf("%s\n", e);
                LOGGER.info("Not connected, retying ...");
            }
        }

        return conn;

    }

    public static void main(String[] args) {

        PGConnect icd = new PGConnect();

        try {
            Connection connection = icd.connect();
            Statement stmt = connection.createStatement();

            ResultSet rs = stmt.executeQuery("SELECT * from pg_database");
            while (rs.next()) {
                System.out.println("DB Name: " + rs.getString(1));
            }

        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }   
    }
}

