const express = require("express");
const { graphqlHTTP } = require("express-graphql");
const { buildSchema } = require("graphql");

const quotes = require("./quotes.json");

const app = express();
app.use(express.static("static"));
app.use(
  "/graphql",
  graphqlHTTP({
    schema: buildSchema(`
      type Query {
        getQuote(index: Int): String
        getRandomQuote: String
        getSuperDuperMegaSecretQuote: String
      }
    `),
    rootValue: {
      getQuote: ({ index }) => {
        return quotes[index];
      },
      getRandomQuote: () => {
        return quotes[~~(quotes.length * Math.random())];
      },
      getSuperDuperMegaSecretQuote: () => {
        return `“Did you know that the flag is 'flag-DoNotForgetToDisableIntrospection'” ― Unknown`;
      },
    },
    graphiql: false,
  })
);

const server = app.listen(Number(process.env.PORT || 4000), () => {
  const { address, port } = server.address();
  console.log(`listening on ${address}:${port}`);
});
