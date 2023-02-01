import './App.css';
import { useState, useEffect } from "react" 

function App() {

  const [fName, setFName] = useState('')
  const [lName, setLName] = useState('')
  const [email, setEmail] = useState('')
  const [phone, setPhone] = useState('')

  useEffect(() => {
    fetch('http://localhost:8000/api//games/')
    .then(r => r.json())
    .then(data => console.log(data))
  })

  function handleClick(){
    fetch('http://localhost:8000/api//address/', {
      method: "POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({
        first_name: fName,
        last_name: lName,
        email: email,
        phone_number: phone
      })
    })
    .then(r => r.json())
    .then(data => console.log(data))
  }

  return (
    <div className="App">
        <input onChange={(e) => setFName(e.target.value)} />
        <input onChange={(e) => setLName(e.target.value)} />
        <input onChange={(e) => setEmail(e.target.value)} />
        <input onChange={(e) => setPhone(e.target.value)} />
        <button onClick={handleClick}>Click</button>
    </div>
  );
}

export default App;
