import React, { useState } from 'react';
import axios from 'axios';

function MyForm() {
  const [formData, setFormData] = useState({});

  const handleSubmit = () => {
    console.log(formData,8)
    axios.post("http://127.0.0.1:8000/post-data", formData)  // 127.0.0.1:3000/post-data   127.0.0.1:8000/post-data
      .then(response => {
        console.log("hello testing");
      })
      .catch(error => {
        console.log("hello errror", error);
      });
  };
  
  const handleChange = (event) => {
    
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };

  return (
    <form>
      <label>
        Item Name:
        <input type="text" name="name" onChange={handleChange} />
      </label> <br/>
      <label>
        Item Price:
        <input type="text" name="price" onChange={handleChange} />
      </label><br/>
      <label>
        Item Status:
        <input type="text" name="status" onChange={handleChange} />
      </label> <br/>
      <button onClick={handleSubmit}>Submit</button>
    </form>
  );
}

export default MyForm;





  //   <div>
  //   <form action="/post-data" method = "POST" onSubmit={handleSubmit}>
  //  <p>Item name <input type = "text" name = "item_name" onChange={handleChange} /></p>
  //  <p>Price <input type = "integer" name = "price" /></p>
  //  <p>Status <input type = "text" name = "item_status" /></p>
  //  <p><input type = "submit" value = "Send" /></p>
  // </form>
  // </div>

    





