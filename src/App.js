import React, { useState, useEffect } from 'react'; 
import axios from 'axios'; 
function App() {
    const [items, setItems] = useState([]); 
    const [newItem, setNewItem] = useState(''); 
      // Fetch items from backend 
      useEffect(() => {
        axios.get('http://localhost:5000/api/showitems').then(response => {
          setItems(response.data);
        }).catch(error => {
          console.error('Error fetching items: ', error); }); }, []); 
          
          // Add a new item 
const addItem = () => {
              if (newItem.trim() === '') return;
              axios.post('http://localhost:5000/api/items', { name: newItem })
                .then(response => {
                  setItems([...items, response.data]);
                  setNewItem('');
                }).catch(error => {
                  console.error('Error adding item: ', error); 
                  });
                   }; 
                   
return ( <div style={{ padding: '20px' }}> 
            < h1 > MySQL React List</h1 > <input type="text" value={newItem} 
onChange={e => setNewItem(e.target.value)} 
placeholder="Add a new item" 
style={{ marginRight: '10px', padding: '5px' }} /> <button 
onClick={addItem} style={{ padding: '5px 10px' }}>Add</button> <ul> 
{items.map(item => ( <li key={item.id}>{item.name}</li> ))} </ul> 
</div > );
                } export default App; 