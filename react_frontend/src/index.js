import React from 'react';
import ReactDOM from 'react-dom/client';
import MyForm from './form1';

const myFirstElement = <h1><MyForm/></h1>

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(myFirstElement);

