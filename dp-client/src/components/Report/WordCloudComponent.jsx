// WordCloudComponent.jsx
import React, { useCallback } from 'react';
import WordCloud from 'react-d3-cloud';
import { scaleOrdinal } from 'd3-scale';
import { schemeCategory10 } from 'd3-scale-chromatic';

const WordCloudComponent = ({ wordCloudData }) => {
    const fontSize = useCallback((word) => Math.log2(word.value) * 5, []);
    const rotate = useCallback((word) => word.value % 360, []);
    const fill = useCallback((d, i) => scaleOrdinal(schemeCategory10)(i), []);

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
            fill={fill}
        />
    );
};

// Ensure the component is exported as default
export default React.memo(WordCloudComponent);
