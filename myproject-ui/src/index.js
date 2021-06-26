import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {Provider} from "react-redux";

import createStore from "./store";

const  store = createStore();

ReactDOM.render(
    <Provider store={createStore()}>
        <App />
    </Provider>,
    document.getElementById('root')
);
