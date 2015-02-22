package wordcloudweb

/**
* Domain class defining a filter for creating a 
* subset of our body of documents. 
**/
class Filter
{
	String name;
	int numPhases; // this might be unused
	//List phases; // a list of Phase domain objects

	//String sortField; // this is gonna become a list
	List<String> sortFields;
	//List allowedValuesList; // this will become list of lists
	//String allowedValues; // this will become list of strings
	List<String> allowedValueStrings;
	List<List> allowedValueLists;

	boolean shouldInvert;

	public Filter()
	{
		sortFields = [];
		allowedValueStrings = [];
		allowedValueLists = [];
	}

	public setName(String name)
	{
		this.name = name;
	}

	public addSortField(String sortField)
	{
		// todo: write me
		this.sortFields.add(sortField);
	}
	
	/*public setSortField(String sortField)
	{
		this.sortField = sortField;
	}*/

	public addAllowedValuesString(String allowedVals)
	{
		// todo: write me
		this.allowedValueStrings.add(allowedVals);
	}

	/*public setAllowedValues(String allowedVals)
	{
		this.allowedValues = allowedVals;
	}*/

	public addAllowedValuesList(List allowedVals)
	{
		this.allowedValueLists.add(allowedVals);
	}
	
	/*public setAllowedValuesList(List allowedVals)
	{
		this.allowedValuesList = allowedVals;
	}*/

	public String getName()
	{
		return this.name;
	}

	public List getSortFields()
	{
		return this.sortFields;
	}

	public List getAllowedValueLists()
	{
		return this.allowedValueLists;
	}

	public List getAllowedValueStrings()
	{
		return this.allowedValueStrings;
	}

	/*public String getSortField()
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
	}*/

}