import axios from 'axios';

/**
 *  上传文件
 * @param params
 * @returns {Promise.<TResult>}
 */
export const  uploadPic = params => {

  return axios.post('/api/upload',params).then(res =>{
    return res.data;
  });
};

export const echo = msg =>{
  return axios.get(`/api/echo/${msg}`).then(res =>{
    return res.data;
  });
}


export const log = msg => {
  console.log(`${Date.now()} ${msg}`);
};
