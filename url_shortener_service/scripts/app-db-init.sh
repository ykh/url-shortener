set -e

echo '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
echo 'Mongo init script is running ... >>>'
echo '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'

mongosh <<EOF
db = db.getSiblingDB('$MONGO_APP_DB_NAME')

db.createUser({
  user: '$MONGO_APP_DB_USER',
  pwd: '$MONGO_APP_DB_PASSWORD',
  roles: [
    { role: 'readWrite', db: '$MONGO_APP_DB_NAME' },
    { role: 'dbAdmin', db: '$MONGO_APP_DB_NAME' },
    { role: 'userAdmin', db: '$MONGO_APP_DB_NAME' }
  ],
});

db = db.getSiblingDB('$MONGO_TEST_DB_NAME')

db.createUser({
  user: '$MONGO_TEST_DB_USER',
  pwd: '$MONGO_TEST_DB_PASSWORD',
  roles: [
    { role: 'readWrite', db: '$MONGO_TEST_DB_NAME' },
    { role: 'dbAdmin', db: '$MONGO_TEST_DB_NAME' },
    { role: 'userAdmin', db: '$MONGO_TEST_DB_NAME' }
  ],
});

EOF

echo '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
echo 'Mongo init script finished. <<<'
echo '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'