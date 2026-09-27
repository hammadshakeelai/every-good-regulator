-- Start every level-1 heading (Parts, chapters, interludes, appendices) on a new page.
local first = true
function Header(el)
  if el.level ~= 1 then return nil end
  -- (Word: page breaks come from the Heading 1 style in build/reference.docx)
  if FORMAT:match("html") or FORMAT:match("epub") then
    el.attributes["style"] = "page-break-before: always; break-before: page;"
    return el
  end
end
