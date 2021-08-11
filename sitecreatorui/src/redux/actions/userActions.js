import {ActionTypes} from "../constants/action-types";


export const setUsers = (users) => {
    return{
        type: ActionTypes.SET_USERS,
        payload:users,
    };
};


export const selectedUser = (user) => {
    return{
        type: ActionTypes.SELECTED_USER,
        payload: user,
    };
};

export const removeSelectedUser = () => {
    return{
        type: ActionTypes.REMOVE_SELECTED_USER,
    };
};