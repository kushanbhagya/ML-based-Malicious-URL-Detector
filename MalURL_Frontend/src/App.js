import React, { useState } from 'react';
import './App.css';
import Swal from 'sweetalert2';
import axios from 'axios';

function App() {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState('');

  const handleVerify = () => {
    if (url) {
      axios
        .post('http://localhost:5000/verify', { url })
        .then((response) => {
          setResult(response.data.result);
          // Handle the result here, display messages, etc.
          if (response.data.result === "good") {
            Swal.fire({
              icon: 'success',
              text: `Verifying URL: ${url}`,
              title: response.data.result,
            });
          } else {
            Swal.fire({
              icon: 'warning',
              text: `Verifying URL: ${url}`,
              title: response.data.result,
            });
          }
        })
        .catch((error) => {
          // Handle Axios or other errors here
          console.error(error);
          Swal.fire({
            icon: 'error',
            text: 'An error occurred while verifying the URL.',
            title: 'ERROR',
          });
        });
    } else {
      Swal.fire({
        icon: 'warning',
        text: 'Please enter a URL before verifying.',
        title: 'INVALID!',
      });
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1 className="glitch">MalURL.ai</h1>
        <input
          type="text"
          placeholder="Enter URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={handleVerify}>Verify</button>
      </div>
    </div>
  );
}

export default App;
