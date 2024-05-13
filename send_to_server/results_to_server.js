const yaml = require("js-yaml");
const fs = require('fs');
const axios = require('axios');

try {
    const yaml_file = yaml.readFileSync('config.yaml', 'utf8');
    const parsedData = yaml.safeLoad(yaml_file);
    const serverAddress = parsedData.server;
    console.info(parsedData);
} catch (e) {
    console.error(e);
}

const imagePaths = ['../results/1.jpg', '../results/2.jpg', '../results/3.jpg', '../results/4.jpg'];
const videoPath = '../results/1.mp4';

const formData = new FormData();
imagePaths.forEach((imagePath, index) => {
    const fileStream = fs.createReadStream(imagePath);
    formData.append(`image${index + 1}`, fileStream);
});
formData.append('video', fs.createReadStream(videoPath));

const otherData = {
    'user_id': 1,
    'season': 'winter',
    'frame': 1
};
Object.keys(otherData).forEach(key => {
    formData.append(key, otherData[key]);
});

axios.post(serverAddress, formData, {
    headers: {
        'Content-Type': 'multipart/form-data',
    },
})
.then(response => {
    console.log(response.data);
})
.catch(error => {
    console.error('에러 발생:', error);
});