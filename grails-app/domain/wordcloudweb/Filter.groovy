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
	List allowedValuesList;
	String allowedValues;
	boolean shouldInvert;

	public Filter()
	{

	}

	public setName(String name)
	{
		this.name = name;
	}

	public setSortField(String sortField)
	{
		this.sortField = sortField;
	}

	public setAllowedValues(String allowedVals)
	{
		this.allowedValues = allowedVals;
	}

	public setAllowedValuesList(List allowedVals)
	{
		this.allowedValuesList = allowedVals;
	}

	public String getName()
	{
		return this.name;
	}

	public String getSortField()
	{
		return this.sortField;
	}

	public String getAllowedValues()
	{
		return this.allowedValues;
	}

	public List getAllowedValuesList()
	{
		return this.allowedValuesList;
	}

}