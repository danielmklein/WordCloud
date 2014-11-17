package core.javacore;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.Serializable;

/**
 * @author Daniel Klein This class represents a document object (such as a
 *         single Supreme Court opinion). A typical object will consist of the
 *         document's text and a metadata object consisting of various fields
 *         relevant to the document. We will subclass the metadata class for
 *         each type of document we will use.
 */
public class Document implements Serializable
{
    private Metadata docMetadata;
    protected String docText;
    private String outputFilename;
    private int wordCount;

    public Document(Metadata docMetadata, String docText, String outputFilename)
    {

        this.docMetadata = docMetadata;
        this.docText = docText;
        this.outputFilename = outputFilename;
        //this.wordCount = countWords(docText);
    }

    public int countWords(String text)
    {

        return text.split(" ").length;
    }

    public String getOutputFilename()
    {

        return this.outputFilename;
    }

    public String getText()
    {

        return this.docText;
    }

    public Metadata getMetadata()
    {

        return this.docMetadata;
    }

    public void setText(String text)
    {
        this.docText = text;
    }

    public void setOutputFilename(String filename)
    {
        this.outputFilename = filename;
    }

    public void setMetadata(Metadata meta)
    {
        this.docMetadata = meta;
    }

    public void serialize() throws IOException
    {

        ObjectOutputStream oos = null;
        try
        {
            FileOutputStream fout = new FileOutputStream(this.outputFilename);
            oos = new ObjectOutputStream(fout);
            oos.writeObject(this);
        } catch (IOException e)
        {
            e.printStackTrace();
            System.out.println("Oops... something went wrong while serializing a Document object.");
            throw e;
        } finally
        {
            if (oos != null)
            {
                try
                {
                    oos.close();
                } catch (IOException e)
                {
                    e.printStackTrace();
                    System.out.println("Unable to close ObjectOutputStream.");
                }

            }
        }
    }

    public String toString()
    {

        return "";
    }

}
