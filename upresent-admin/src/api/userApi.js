import { handleResponse, handleError } from "./apiUtils";
import { baseUrlUserApi } from "../config/config";

const baseUrl = baseUrlUserApi;

export function getUsers() {
  return fetch(baseUrl + "/all", {
    method: "GET",
    headers: {
      "content-type": "application/json"
    }
  })
    .then(handleResponse)
    .catch(handleError);
}

export function getUserByUsername(username) {
  return fetch(baseUrl + "?username=" + username, {
    method: "GET",
    headers: {
      "content-type": "application/json"
    }
  })
    .then(handleResponse)
    .catch(handleError);
}

export function saveUser(user) {
  if (!user.id) {
    return fetch(baseUrl, {
      method: "POST",
      headers: {
        "content-type": "application/json"
      },
      body: JSON.stringify(user)
    })
      .then(handleResponse)
      .catch(handleError);
  } else {
    return fetch(baseUrl, {
      method: "PUT",
      headers: {
        "content-type": "application/json"
      },
      body: JSON.stringify(user)
    })
      .then(handleResponse)
      .catch(handleError);
  }
}
