```dataviewjs
let page= dv.page("Aves");
let table = [ {N: 1, Clase: "Aves", Orden: "Ciconiiformes", Familia: "Cathartidae", Género: "Vultur", Especie: "Vultur gryphus", NombreComun: "Cóndor Andino", CategoriaUICN: "Casi amenazada"}, {N: 2, Clase: "Aves", Orden: "Ciconiiformes", Familia: "Cathartidae", Género: "Coragyps", Especie: "Coragyps atratus", NombreComun: "Jote Cabeza Negra", CategoriaUICN: "Preocupación Menor"}, {N: 3, Clase: "Aves", Orden: "Falconiformes", Familia: "Accipitridae", Género: "Geranoaetus", Especie: "Geranoaetus melanoleucus", NombreComun: "Águila", CategoriaUICN: "Preocupación Menor"} ];

let filteredTable = table.filter(row => row.Familia === "Cathartidae"); 

dv.table(["N°", "Clase", "Orden", "Familia", "Género", "Especie", "Nombre(s) Común(es)", "Categoría UICN"], filteredTable.map(row => [row.N, row.Clase, row.Orden, row.Familia, row.Género, row.Especie, row.NombreComun, row.CategoriaUICN]));

```
