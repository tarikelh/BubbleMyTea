const baseUrl = 'http://localhost:8000';

const jsonOrThrowIfError = async response => {
  if(!response.ok) throw new Error((await response.json()).message);
  return response.json();
};

export const fetchData = async ({ endpoint, init }) => jsonOrThrowIfError(await fetch(`${baseUrl + endpoint}`, init));
