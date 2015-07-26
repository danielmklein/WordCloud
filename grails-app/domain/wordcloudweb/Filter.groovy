package wordcloudweb

/**
* Domain class defining a filter for creating a
* subset of our body of documents.
**/
class Filter
{
	String name;
	int numPhases; // this might be unused

	List<String> sortFields;
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
		this.sortFields.add(sortField);
	}

	public addAllowedValuesString(String allowedVals)
	{
		this.allowedValueStrings.add(allowedVals);
	}

	public addAllowedValuesList(List allowedVals)
	{
		this.allowedValueLists.add(allowedVals);
	}

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

}
