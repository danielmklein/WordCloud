dataSource {
    pooled = true
    jmxExport = true
}
hibernate {
    cache.use_second_level_cache = true
    cache.use_query_cache = false
//    cache.region.factory_class = 'net.sf.ehcache.hibernate.EhCacheRegionFactory' // Hibernate 3
    cache.region.factory_class = 'org.hibernate.cache.ehcache.EhCacheRegionFactory' // Hibernate 4
    singleSession = true // configure OSIV singleSession mode
    flush.mode = 'manual' // OSIV session flush mode outside of transactional context
}

// environment specific settings
environments {
    test {
        dataSource {
            driverClassName = "org.h2.Driver"
            dbCreate = "create-drop" // one of 'create', 'create-drop', 'update', 'validate', ''
            url = "jdbc:h2:mem:devDb;MVCC=TRUE;LOCK_TIMEOUT=10000;DB_CLOSE_ON_EXIT=FALSE"
        }
    }

    development {
        dataSource {
            username = "[username_here]"
            password = "[password_here]"

            dbCreate = "create-drop"
            url = "jdbc:mysql://[endpoint]:[port]/[database]?useUnicode=yes&characterEncoding=UTF-8"
            driverClassName = "com.mysql.jdbc.Driver"
            dialect = "org.hibernate.dialect.MySQL5InnoDBDialect"
            pooled = true

            properties {
               // See http://grails.org/doc/latest/guide/conf.html#dataSource for documentation
               jmxEnabled = true
               initialSize = 5
               maxActive = 50
               minIdle = 5
               maxIdle = 25
               maxWait = 10000
               maxAge = 10 * 60000
               timeBetweenEvictionRunsMillis = 180000
               numTestsPerEvictionRun = 3
               minEvictableIdleTimeMillis = 180000
               validationQuery = "SELECT 1"
               validationQueryTimeout = 3
               validationInterval = 15000
               testOnBorrow = true
               testWhileIdle = true
               testOnReturn = true
               jdbcInterceptors = "ConnectionState"
               defaultTransactionIsolation = java.sql.Connection.TRANSACTION_READ_COMMITTED
            }
        }
        hibernate {
            show_sql = true
        }
    }
    production {
        dataSource {
            username = "[username_here]"
            password = "[password_here]"

            dbCreate = "create-drop"
            url = "jdbc:mysql://[endpoint]:[port]/[database]?useUnicode=yes&characterEncoding=UTF-8"
            driverClassName = "com.mysql.jdbc.Driver"
            dialect = "org.hibernate.dialect.MySQL5InnoDBDialect"
            pooled = true

            properties {
               // See http://grails.org/doc/latest/guide/conf.html#dataSource for documentation
               jmxEnabled = true
               initialSize = 5
               maxActive = 50
               minIdle = 5
               maxIdle = 25
               maxWait = 10000
               maxAge = 10 * 60000
               timeBetweenEvictionRunsMillis = 180000
               numTestsPerEvictionRun = 3
               minEvictableIdleTimeMillis = 180000
               validationQuery = "SELECT 1"
               validationQueryTimeout = 3
               validationInterval = 15000
               testOnBorrow = true
               testWhileIdle = true
               testOnReturn = true
               jdbcInterceptors = "ConnectionState"
               defaultTransactionIsolation = java.sql.Connection.TRANSACTION_READ_COMMITTED
            }
        }
    }
}
