# byescaleira apps

Source de AltStore e SideStore com os apps de sideload do Rafael Escaleira.

**URL do source:** `https://byescaleira.github.io/apps/source.json`

No AltStore: Browse › Sources › `+` e cole a URL (ou abra https://byescaleira.github.io/apps e toque em "Add to AltStore").

## Apps

| App | Repositório |
| --- | --- |
| IPA | [byescaleira/ipa](https://github.com/byescaleira/ipa) |

## Publicar uma versão

Cada app gera o `.ipa` sem assinatura, anexa a um GitHub Release do próprio repositório e acrescenta a versão aqui:

```sh
scripts/add-version.py <bundle id> <versão> <build> <url do .ipa> <tamanho em bytes> --min-os 27.0 --notes "<novidades>"
```

No IPA, `scripts/release.sh` faz tudo isso de uma vez.
