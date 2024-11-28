import React, { useCallback } from 'react';
import WordCloud from 'react-d3-cloud';

const WordCloudComponent = ({ wordCloudData }) => {
    // Adjusted font size for smaller words
    const fontSize = useCallback((word) => Math.log2(word.value) * 3, []); // Reduced size multiplier
    const rotate = useCallback(() => 0, []); // No rotation for uniform layout

    return (
        <div style={{}}>
            <WordCloud
                data={wordCloudData.map((word, index) => ({
                    ...word,
                    text: word.text,
                    color: index % 2 === 0 ? '#7f00ff' : '#B369FE', // Alternating pink tones
                }))}
                font="Pretendard" // Friendly and rounded font
                fontStyle="normal"
                fontWeight="bold"
                fontSize={fontSize}
                spiral="archimedean" // Better distribution for text
                rotate={rotate} // No rotation
                padding={5}
                random={Math.random}
                fill={(d) => d.color} // Using color directly from data
            />
        </div>
    );
};

export default React.memo(WordCloudComponent);
