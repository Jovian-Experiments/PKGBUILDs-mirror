# Maintainer: Jo Bates <jo@valvesoftware.com>
# Maintainer: Manuel A. Fernandez Montecelo <mafm@igalia.com>

pkgname=vpower
pkgver=1.6.1
pkgrel=1
pkgdesc="Service that calculates battery metrics and handles critical battery scenarios"
url=https://gitlab.steamos.cloud/jupiter/vpower
arch=(x86_64)
license=(MIT)
depends=(gcc-libs lm_sensors systemd-sysvcompat)
makedepends=(rust git openssh)
source=("git+ssh://git@gitlab.steamos.cloud/jupiter/vpower.git#tag=$pkgver"
        crate-lazy_static-1.5.0.tar.gz::https://static.crates.io/crates/lazy_static/1.5.0/download
        crate-libc-0.2.172.tar.gz::https://static.crates.io/crates/libc/0.2.172/download
        crate-proc-macro2-1.0.95.tar.gz::https://static.crates.io/crates/proc-macro2/1.0.95/download
        crate-quote-1.0.40.tar.gz::https://static.crates.io/crates/quote/1.0.40/download
        crate-serde-1.0.219.tar.gz::https://static.crates.io/crates/serde/1.0.219/download
        crate-serde_derive-1.0.219.tar.gz::https://static.crates.io/crates/serde_derive/1.0.219/download
        crate-syn-2.0.101.tar.gz::https://static.crates.io/crates/syn/2.0.101/download
        crate-toml-0.5.8.tar.gz::https://static.crates.io/crates/toml/0.5.8/download
        crate-unicode-ident-1.0.18.tar.gz::https://static.crates.io/crates/unicode-ident/1.0.18/download
       )
sha256sums=('SKIP'
            'bbd2bcb4c963f2ddae06a2efc7e9f3591312473c50c6685e1f298068316e66fe'
            'd750af042f7ef4f724306de029d18836c26c1765a54a6a3f094cbd23a7267ffa'
            '02b3e5e68a3a1a02aad3ec490a98007cbc13c37cbe84a3cd7b8e406d76e7f778'
            '1885c039570dc00dcb4ff087a89e185fd56bae234ddc7f056a945bf36467248d'
            '5f0e2c6ed6606019b4e29e69dbaba95b11854410e5347d525002456dbbb786b6'
            '5b0276cf7f2c73365f7157c8123c21cd9a50fbbd844757af28ca1f5925fc2a00'
            '8ce2b7fc941b3a24138a0a7cf8e858bfc6a992e7978a068a5c760deb0ed43caf'
            'a31142970826733df8241ef35dc040ef98c679ab14d7c3e54d827099b3acecaa'
            '5a5f39404a5da50712a4c1eecf25e90dd62b613502b7e925fd4e4d19b5c96512'
           )

prepare() {
  # Mark crates as already checksummed
  for x in */.cargo_vcs_info.json \
           vpower/Cargo.toml
  do
    echo '{"files":{}}' > "$(dirname "$x")"/.cargo-checksum.json
  done
  rm vpower/Cargo.lock

  # Tell rust to use the pre-vendored crates
  cd vpower
  mkdir -p .cargo
  touch .cargo/config.toml
  if ! grep -E '^\s*\[source\.crates-io\]\s*' .cargo/config.toml
  then
      cat << EOF >> .cargo/config.toml
    [source.crates-io]
    replace-with = "vendored-sources"

    [source.vendored-sources]
    directory = "${srcdir}"
EOF
  fi
}

build() {
  cd vpower
  cargo build --offline --release
}

package() {
  cd vpower
  install -Dm 755 target/release/vpower -t "$pkgdir/usr/lib"
  install -Dm 644 vpower.toml -t "$pkgdir/etc"
  install -Dm 644 vpower.service -t "$pkgdir/usr/lib/systemd/system"
  install -dm 755 "$pkgdir/usr/lib/systemd/system/graphical.target.wants"
  ln -s ../vpower.service "$pkgdir/usr/lib/systemd/system/graphical.target.wants/vpower.service"
}
