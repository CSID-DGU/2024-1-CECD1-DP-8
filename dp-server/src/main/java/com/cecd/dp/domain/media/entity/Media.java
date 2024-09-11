package com.cecd.dp.domain.media.entity;

import com.cecd.dp.domain.hashtag.entity.HashTag;
import com.cecd.dp.domain.image.entity.Image;
import com.cecd.dp.domain.influencer.entity.Influencer;
import com.cecd.dp.domain.mediahashtag.entity.MediaHashTag;
import com.cecd.dp.global.BaseEntity;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@NoArgsConstructor
public class Media extends BaseEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "media_id")
    private Long id;
    @Lob @Column(columnDefinition = "text")
    private String caption;
    private Integer likeCnt;
    private Integer replyCnt;
    private String type; // 게시글 유형
    private String graphMediaId; // Graph API 조회 미디어 아이디
    private LocalDateTime postedAt;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "influencer_id")
    private Influencer influencer;

    @OneToMany(mappedBy = "media", cascade = CascadeType.ALL)
    private List<MediaHashTag> mediaHashTagList = new ArrayList<>();

    @OneToMany(mappedBy = "media", cascade = CascadeType.ALL)
    private List<Image> imageList = new ArrayList<>();


    //===생성자===//
    @Builder
    public Media(Long id, String caption, Integer likeCnt, Integer replyCnt, String type, String graphMediaId, LocalDateTime postedAt, Influencer influencer) {
        this.id = id;
        this.caption = caption;
        this.likeCnt = likeCnt;
        this.replyCnt = replyCnt;
        this.type = type;
        this.graphMediaId = graphMediaId;
        this.postedAt = postedAt;
        this.influencer = influencer;
    }

    //===연관 관계 보조 메서드===//
    public void setInfluencer(Influencer influencer) {
        this.influencer = influencer;
    }

    //===연관관계 편의 메서드===//
    public void addImage(Image image) {
        if (this.imageList.contains(image)) {
            imageList.remove(image);
        }

        image.setMedia(this);
        this.imageList.add(image);
    }

    public void addMediaHashTag() {

    }
}
