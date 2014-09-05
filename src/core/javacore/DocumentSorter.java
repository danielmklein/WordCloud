package core.javacore;

import java.io.IOException;
import java.util.List;

/**
 * Daniel Klein Computer-Based Honors Program The University of Alabama 9.5.2014
 * 
 * Given a collection of Document objects and a sort key (which is a field of
 * the appropriate metadata object), this will yield subsets of document
 * objects, each subset having the same value for the sort field.
 */
public class DocumentSorter
{

    private List<Document> docList;

    /**
     * @param docList
     */
    public DocumentSorter(List<Document> docList)
    {

        this.docList = docList;
    }

    /**
     * Given a sort_field on which to sort, this will return a list of lists of
     * Document objects, grouped by sort_field value.
     * 
     * @param sortField
     * @return
     * @throws IOException
     */
    public List<List<Document>> sortDocs(String sortField) throws IOException
    {

        throw new IOException("sortDocs hasn't been written yet!");
    }

    /**
     * Given a sort field and a list of values to accept for that field, this
     * will return a list of Document objects, each of whose value for the sort
     * field is in the list of allowedVals. If shouldInvert=True, this will
     * return the set of documents whose value for sortField != anything in
     * allowedVals.
     * 
     * @param sortField
     * @param allowedVals
     * @param shouldInvert
     */
    public List<Document> createSubset(String sortField,
                    List<String> allowedVals, boolean shouldInvert)
                    throws IOException
    {

        throw new IOException("createSubset hasn't been written yet!");
    }

    /**
     * Add a Document object to this.docList.
     * 
     * @param docToAdd
     */
    public void addDoc(Document docToAdd)
    {

        this.docList.add(docToAdd);
    }

    /**
     * Explicitly set this.docList.
     * 
     * @param docToAdd
     */
    public void setDocList(List<Document> newDocs)
    {

        this.docList = newDocs;
    }

}
