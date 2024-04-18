# Maintainer (Holo): Manuel A. Fernandez Montecelo <mafm@igalia.com>

pkgname=holo-glibc-locales
pkgver=2.39
pkgrel=1
pkgdesc="Substitute of glibc-locales with only the locales present in SteamOS"
arch=('x86_64')
license=(GPL LGPL)
provides=(
  "glibc-locales=${pkgver}-${pkgrel}"
)
conflicts=(
  "glibc-locales"
)
replaces=(
  "glibc-locales"
)
source=("https://archive.archlinux.org/packages/g/glibc-locales/glibc-locales-${pkgver}-${pkgrel}-x86_64.pkg.tar.zst")
b2sums=("acc331f48c1f8d7b9eab7d2d6ac11a5d68be96918152deb16773ac446420cf6f63a1f8e55617accfd0c57d30106a3a3c15360567aff4fb2f70cb4cbd0813491d")

package() {
  # runtime depends only
  depends=("glibc=${pkgver}")

  echo "Preparing final destination to create the package"
  local destdir="${pkgdir}"/usr/lib/locale
  install -vdm 755 "${destdir}"

  cd "${srcdir}/usr/lib/locale"

  # from https://gitlab.steamos.cloud/holo/holo/-/commit/fe318d980c317778f7a40eccdc3f24bf4634fb01
  local locales_supported=(
    bg cs da de el en es fi fr hu it ja ko nb nl pl pt ro ru sv th tr uk vi zh
  )

  echo "Moving files to final destination"
  for lang in "${locales_supported[@]}"; do
    # Copy xx_YY.utf8 for every supported language (if exists...)
    for dir in "${lang}"_??.utf8; do
      if [ -d "${dir}" ]; then
        # block with 'install's equivalent to: cp -av "${dir}" "${destdir}"
        install -vdm 755 "${destdir}/${dir}"
        for elem in "${dir}"/*; do
          if [ -d "${elem}" ]; then
            install -vdm 755 "${destdir}/${elem}"
            install -vm 644 "${elem}"/* "${destdir}/${elem}"
          else
            install -vDm 644 "${elem}" "${destdir}/${dir}"
          fi
        done
      fi
    done
    # ... or xx_YY if the '.utf8' one does not exist
    for dir in "${lang}"_??; do
      if [ ! -d "${dir}.utf8" -a -d "${dir}" ]; then
        # block with 'install's equivalent to: cp -av "${dir}" "${destdir}"
        install -vdm 755 "${destdir}/${dir}"
        for elem in "${dir}"/*; do
          if [ -d "${elem}" ]; then
            install -vdm 755 "${destdir}/${elem}"
            install -vm 644 "${elem}"/* "${destdir}/${elem}"
          else
            install -vDm 644 "${elem}" "${destdir}/${dir}"
          fi
        done
      fi
    done
  done

  # deduplicate locale data
  hardlink -c "${pkgdir}/usr/lib/locale"
}

# vim: ts=2 sw=2 et:
