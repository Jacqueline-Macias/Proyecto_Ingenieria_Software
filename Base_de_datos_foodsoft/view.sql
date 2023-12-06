USE foodsoft;

CREATE VIEW vista_icomprainsumo AS
SELECT icompra.id_icompra,insumo.nombre, proveedor.id_proveedor,insumo.precio,icomprainsumo.cantidad
FROM insumo, proveedor, icompra, icomprainsumo
WHERE insumo.id_proveedor = icompra.id_proveedor 
AND icompra.id_proveedor = proveedor.id_proveedor
AND icompra.id_icompra =icomprainsumo.id_icompra 
AND icomprainsumo.insumo = insumo.nombre;

