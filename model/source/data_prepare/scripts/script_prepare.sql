

-- PRODUCT FEATURES

DROP TABLE IF EXISTS #Prod_Features;

SELECT top 10 
cuc as id_producto,
desmarca,
descategoria

INTO #Prod_Features
FROM dom_customer.ecm_res_orden
WHERE sap_codmarket=''
 AND sap_fechafactura >='{fecha_inicio}'
 AND sap_fechafactura <='{fecha_actual}'
 AND sap_flagfacturaanulada='N'
 AND flg_orden='S'
 AND sap_tipodocumento='M'
 AND sap_flagempaque='N'
GROUP BY 1,2,3
HAVING SUM(sap_dunidadesvendidas)>'0';


unload ('select * from #Prod_Features')
to 's3://{bucket_model}/{folder_model}/data-prepare/product-features/data'
iam_role 'arn:aws:iam::820233355588:role/RedshiftS3Role-{env_upper}-BIGDATA'
header
format csv
ALLOWOVERWRITE
PARALLEL OFF;


