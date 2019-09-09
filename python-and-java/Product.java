public class Product {
    
    private int id;
    private String name;
    private String description;
    private double price;

        public Product()
    {     
    }

    public Product(int id, String name, String        
                        description, double price)
    {
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
    }

    public int getid()
    {
            return id;
    }
    public void setid(int id)
    {
        this.id = id;
    }
    public String getname()
    {
        return name;
    }

    public void setname(String name)
    {
        this.name = name;
    }

     public String getdescription()
     {
        return description;
     }

     public void setdescription(String description)
    {
        this.description = description;
    }
    public double getPrice()
    {
        return price;
    }
    public void setPrice(double price)
    {
        this.price = price;
    }

    public String toString()
    {
        return id + " " + name + " " + description + " " + " " + price;
    }
}