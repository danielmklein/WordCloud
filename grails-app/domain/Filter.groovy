package wordcloudweb

/**
* Domain class defining a filter for creating a 
* subset of our body of documents. 
**/
class Filter
{
	String name;
	int numPhases;
	//List phases; // a list of Phase domain objects
	String sortField;
	//List allowedValues;
	String allowedValues;
	boolean shouldInvert;
}