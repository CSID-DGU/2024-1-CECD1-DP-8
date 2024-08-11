package com.cecd.dp.domain.hashtag.entity;

import com.cecd.dp.domain.mediahashtag.entity.MediaHashTag;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@NoArgsConstructor
public class HashTag {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "hash_tag_id")
    private Long id;

    private String name; //태그명

    @OneToMany(mappedBy = "hashTag")
    private List<MediaHashTag> mediaHashTagList = new ArrayList<>();

    @Builder
    public HashTag(String name) {
        this.name = name;
    }

}
