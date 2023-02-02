SELECT  transaction.idTransaction
       ,transaction.step
       ,transaction.type
       ,transaction.amount
       ,origin.NAME
       ,origin.balance   AS "oldBalanceOrig"
       ,transaction.newBalanceOrig
       ,receiver.NAME
       ,receiver.balance AS "oldBalanceDest"
       ,transaction.newBalanceDest
       ,transaction.isFraude
FROM transaction
INNER JOIN origins
ON transaction.idOrigin = origin.idOrigin
INNER JOIN receiver
ON transaction.idReceiver = receiver.idReceiver;