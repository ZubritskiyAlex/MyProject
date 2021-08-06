import {ActionTypes} from "../constants/action-types";

const initialState = {
    shops: [
        {
            id:1,
            title: "TechnoStore",
            description:"device shop",
        }
    ],
};

export const shopReducer = (state= initialState, {type, payload}) =>{
    switch (type){
        case ActionTypes.SET_SHOPS:
            return state;
        default:
            return state;
    }
};