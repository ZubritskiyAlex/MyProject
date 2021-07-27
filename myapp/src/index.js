import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import {createStore} from "redux";

import App from './App';


const initialState =[
  'Hoodie',
  'Laptop'

];



function shop(state = initialState, action){
    if (action.type ==='ADD_PRODUCT'){
        return [
            ...state,
            action.payload
        ];
    }
    return state;
}
const store = createStore(shop);

ReactDOM.render(
  <Provider store={store}>
    <App />,
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