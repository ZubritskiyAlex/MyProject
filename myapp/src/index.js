import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import {createStore} from "redux";

import App from './App';
import reducer from './reducers';


const store = createStore(reducer, window.__REDUX_DEVTOOLS_EXTENSION__&&
    window.__REDUX_DEVTOOLS_EXTENSION__());
ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
 );


// import {createStore} from "redux";
//

//
// const addProductBtn = document.querySelectorAll('.addProduct')[0];
// const productInput = document.querySelectorAll('.productInput')[0];
// const list = document.querySelectorAll('.list')[0];
//
//
// store.subscribe(() => {
//     list.innerHTML = '';
//     productInput.value = '';
//     store.getState().forEach(product => {
//         const li = document.createElement('li');
//         li.textContent=product;
//         list.appendChild(li);
//     })
// })
//
// addProductBtn.addEventListener('click', () => {
//     const productName = productInput.value;
//     store.dispatch({type:'ADD_PRODUCT', payload: productName});
// });