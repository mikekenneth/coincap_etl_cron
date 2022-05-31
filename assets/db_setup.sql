DROP TABLE IF EXISTS crypto.exchange;
DROP SCHEMA IF EXISTS crypto;
CREATE SCHEMA crypto;
CREATE TABLE crypto.exchange (
    batchId VARCHAR(50),
    batchDatetime TIMESTAMP,
    id VARCHAR(50),
    name VARCHAR(50),
    rank INT,
    percentTotalVolume NUMERIC(8, 5),
    volumeUsd NUMERIC,
    tradingPairs INT,
    socket BOOLEAN,
    exchangeUrl VARCHAR(50),
<<<<<<< HEAD
    updated BIGINT,
=======
    updatedUnixmillis BIGINT,
>>>>>>> 433f1ec813f0537a8ad3bea1523e25b63a5662cf
    updatedUTC TIMESTAMP
);