package com.cecd.dp.domain.mediahashtag.entity;

import com.cecd.dp.domain.hashtag.entity.HashTag;
import com.cecd.dp.domain.media.entity.Media;
import jakarta.persistence.*;
import lombok.Getter;

@Entity
@Getter
public class MediaHashTag {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "media_hash_tag_id")
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY, cascade = CascadeType.ALL)
    @JoinColumn(name = "hash_tag_id")
    private HashTag hashTag;

    @ManyToOne(fetch = FetchType.LAZY, cascade = CascadeType.ALL)
    @JoinColumn(name = "media_id")
    private Media media;

    //===연관관계 편의 메서드===//
    public void setHashTag(HashTag hashTag) {

        this.hashTag = hashTag;
        hashTag.getMediaHashTagList().add(this);
    }

    public void setMedia(Media media) {
/*        if (!media.getMediaHashTagList().isEmpty()) {
            if(media.getMediaHashTagList().contains(media)) media.getMediaHashTagList().remove(media);
        }*/

        this.media = media;
        this.media.getMediaHashTagList().add(this);
    }
}
