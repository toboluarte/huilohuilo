```dataviewjs
// Crear un array con los datos de la tabla
let table = [
 data = {
 }

// Filtrar la tabla por la Familia Cathartidae
let filteredTable = table.filter(row => row.Familia === "Cathartidae");

// Mostrar los resultados filtrados en una tabla
dv.table(["N°", "Clase", "Orden", "Familia", "Especie", "Nombre(s) Común(es)"],
    filteredTable.map(row => [row.N, row.Clase, row.Orden, row.Familia, row.Especie, row.NombreComun]));

```
