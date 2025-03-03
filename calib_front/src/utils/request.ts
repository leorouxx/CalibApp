export async function requestGet<T>(url: string): Promise<T> {
    try {
        const response = await fetch(url);
      
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
  
        const data = await response.json();
        return data

    } 
    catch (error) {
        console.error(`Error fetching data to ${url}:`, error);
        throw error;
    }
}

export async function requestPost<T>(url: string, body: object): Promise<T> {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(body)
        });
      
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
  
        const data = await response.json();
        return data

    } 
    catch (error) {
        console.error(`Error fetching data to ${url}:`, error);
        throw error;
    }
}