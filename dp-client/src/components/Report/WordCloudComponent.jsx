import React, { useCallback } from 'react';
import WordCloud from 'react-d3-cloud';

// Custom gradient color function
const gradientColor = (index) => {
    const gradient = `linear-gradient(90deg, rgba(74, 58, 255, 0.80) 0%, rgba(102, 48, 170, 0.80) 100%)`;
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    const gradientFill = context.createLinearGradient(0, 0, 300, 0);

    // Parse colors and add to gradient
    gradientFill.addColorStop(0, 'rgba(74, 58, 255, 0.80)');
    gradientFill.addColorStop(1, 'rgba(102, 48, 170, 0.80)');

    return gradientFill;
};

const WordCloudComponent = ({ wordCloudData }) => {
    // Reduced font size by ~5px
    const fontSize = useCallback((word) => Math.log2(word.value) * 3.5, []); // Adjusted multiplier to reduce size
    const rotate = useCallback((word) => word.value % 360, []);

    return (
        <WordCloud
            data={wordCloudData}
            width={500}
            height={500}
            font="Times"
            fontStyle="italic"
            fontWeight="bold"
            fontSize={fontSize}
            spiral="rectangular"
            rotate={rotate}
            padding={5}
            random={Math.random}
            fill={gradientColor} // Applying gradient color
        />
    );
};

export default React.memo(WordCloudComponent);
