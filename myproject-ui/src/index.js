import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {Provider} from "react-redux";
import 'semantic-ui-css/semantic.min.css';
import createStore from "./store";
import './app.css';

const  store = createStore();

ReactDOM.render(
    <Provider store={createStore()}>
        <App />
    </Provider>,
    document.getElementById('root')
);
