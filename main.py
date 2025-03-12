import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import liquibase.Liquibase;
import liquibase.database.Database;
import liquibase.database.jvm.HibernateDatabase;
import liquibase.resource.ClassLoaderResourceAccessor;
import java.sql.Connection;
import java.util.logging.Logger;

public class MigrationManager {
    private static final Logger logger = Logger.getLogger("MigrationManager");
    private static SessionFactory sessionFactory;

    public static void main(String[] args) {
        try {
            sessionFactory = new Configuration().configure("
